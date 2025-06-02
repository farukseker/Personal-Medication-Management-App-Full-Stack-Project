self.addEventListener('push', function (event) {
  let data = { title: 'Bildirim Var!', body: 'Yeni bir mesajınız var.' };

  if (event.data) {
    try {
      data = event.data.json();
    } catch(e) {
      // JSON parse hatası varsa fallback kullan
      data.body = event.data.text();
    }
  }

  const title = data.title || 'Bildirim Var!';
  const options = {
    body: data.body || '',
    icon: '/icons/launchericon-144-144.png',
    badge: '/icons/launchericon-144-144.png'
  };

  event.waitUntil(
    self.registration.showNotification(title, options)
  );
});
