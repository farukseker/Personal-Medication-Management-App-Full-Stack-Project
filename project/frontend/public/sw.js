self.addEventListener('push', function (event) {
  event.waitUntil(
    (async () => {
      let data = {
        title: 'Bildirim Var!',
        body: 'Yeni bir mesajınız var.',
        type: 'default',
      };

      if (event.data) {
        try {
          const textData = await event.data.text();
          console.log('Raw push payload:', textData);

          const parsedData = JSON.parse(textData);
          console.log('Parsed:', parsedData);
          console.log('typeof:', typeof parsedData);
          console.log('keys:', Object.keys(parsedData));

          data = parsedData;
        } catch (e) {
          console.error('Push verisi parse edilemedi:', e);
        }
      }

      let title = data.title || 'Bildirim';
      let body = data.body || '';
      let actions = [];

      // Bildirim türüne göre özelleştirme
      switch (data.type) {
        case 'medicine':
          title = 'İlaç Hatırlatması';
          body = data.body || 'İlacınızı almayı unutmayın!';
          actions = [
            { action: 'take', title: 'Aldım' },
            { action: 'skip', title: 'Pas Geç' },
          ];
          break;

        case 'weight':
          title = 'Tartılma Zamanı';
          body = data.body || 'Bugün tartıldınız mı?';
          break;

        case 'water':
          title = 'Su İçmeyi Unutma';
          body = data.body || 'Bir bardak su içmeyi ihmal etme!';
          break;

        default:
          // Diğer durumlar için varsayılan bırak
          break;
      }

      const options = {
        body: body,
        icon: data.profile_picture || '/icons/launchericon-144-144.png',
        badge: '/icons/launchericon-144-144.png',
        image: data.profile_picture || undefined,
        actions: actions,
        data: {
          url: data.url || '/',
          type: data.type,
        },
      };

      self.registration.showNotification(title, options);
    })()
  );
});

// click
async function fetchWithRefresh(url, options = {}) {
  const response = await fetch(url, {
    ...options,
    credentials: 'include',
  });

  if (response.status === 401) {
    const refreshResponse = await fetch('/auth/refresh', {
      method: 'POST',
      credentials: 'include', 
    });
    console.log(refreshResponse)
    if (!refreshResponse.ok) {
      console.error('Refresh başarısız, oturum süresi dolmuş olabilir');
      return response;
    }

    return await fetch(url, {
      ...options,
      credentials: 'include',
    });
  }

  return response;
}

self.addEventListener('notificationclick', function (event) {
  event.notification.close();

  const action = event.action;
  const type = event.notification.data?.type;
  const urlToOpen = event.notification.data?.url || '/';

  if (action === 'take') {
    event.waitUntil(
      fetch('https://api.siten.com/medicine/take/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: 'include',  // 🍪 Cookie içindeki JWT otomatik gönderilir
        body: JSON.stringify({
          timestamp: new Date().toISOString(),
          type: type || 'medicine',
        }),
      })
        .then((res) => {
          if (!res.ok) throw new Error('API çağrısı başarısız');
          return res.json();
        })
        .then((data) => console.log('API yanıtı:', data))
        .catch((err) => console.error('API hatası:', err))
    );
  } else if (action === 'skip') {
    console.log('Kullanıcı pas geçti.');
  } else {
    // Bildirime normal tıklanırsa pencereyi aç
    event.waitUntil(
      clients.matchAll({ type: 'window', includeUncontrolled: true }).then((clientList) => {
        for (let client of clientList) {
          if (client.url === urlToOpen && 'focus' in client) {
            return client.focus();
          }
        }
        if (clients.openWindow) {
          return clients.openWindow(urlToOpen);
        }
      })
    );
  }
});
