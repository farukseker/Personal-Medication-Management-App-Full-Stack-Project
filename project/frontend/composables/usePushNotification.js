// frontend/composables/usePushNotification.js
export const usePushNotification = () => {
  const vapidPublicKey = "BEY_xESeYvlT7oBJhcktblnG9JKHNEzqg8UgBsydPVh51Wx_OnfaP7EXRXkRrR7PgaX2ivjJYwMZkxZRmQIhJPc";

  const urlBase64ToUint8Array = (base64String) => {
    const padding = '='.repeat((4 - base64String.length % 4) % 4);
    const base64 = (base64String + padding).replace(/-/g, '+').replace(/_/g, '/');
    const rawData = atob(base64);
    return Uint8Array.from([...rawData].map(c => c.charCodeAt(0)));
  };
  
  const subscribe = async () => {
    if (!('serviceWorker' in navigator)) {
      console.warn('Tarayıcı service worker desteklemiyor. Abonelik iptal edildi.');
      return;
    }

    const permission = await Notification.requestPermission();
    if (permission !== 'granted') {
      console.warn('Kullanıcı bildirim izni vermedi. Abonelik iptal edildi.');
      return;
    }

    try {
      const registration = await navigator.serviceWorker.register('/sw.js');
      console.log('Service Worker kaydedildi:', registration);

      const existing = await registration.pushManager.getSubscription();
      if (existing) {
        console.log('Zaten aktif bir aboneliğin var:', existing);
        return;
      }

      const applicationServerKey = urlBase64ToUint8Array(vapidPublicKey);
      
      const newSub = await registration.pushManager.subscribe({
        userVisibleOnly: true,
        applicationServerKey: applicationServerKey
      });
      console.log('Yeni abonelik oluşturuldu:', newSub);

      // Backend'e sadece Subscription nesnesini gönderiyoruz.
      try {
        const { $api } = useNuxtApp()
        const data = await $api('/notification/subscribe/',{
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(newSub)
          }
        )

        // await $fetch('/medications/subscribe', {
        //   method: 'POST',
        //   headers: { 'Content-Type': 'application/json' },
        //   body: JSON.stringify(newSub)
        // });
        console.log('Abonelik backend’e gönderildi.');
      } catch (backendErr) {
        console.error('Backend’e abonelik gönderiminde hata:', backendErr);
      }

    } catch (err) {
      console.error('Push aboneliği sırasında hata oluştu:', err.name, err.message);
    }
  };

  const unsubscribe = async () => {
    if (!('serviceWorker' in navigator)) {
      console.warn('Tarayıcı service worker desteklemiyor.');
      return;
    }

    try {
      const registration = await navigator.serviceWorker.getRegistration();
      if (!registration) {
        console.warn('Service Worker kaydı bulunamadı.');
        return;
      }

      const subscription = await registration.pushManager.getSubscription();
      if (!subscription) {
        console.warn('Aktif bir push aboneliği yok.');
        return;
      }

      const success = await subscription.unsubscribe();
      if (success) {
        console.log('Push aboneliği tarayıcıdan iptal edildi.');

        try {
          const { $api } = useNuxtApp()
          await $api('/notification/unsubscribe/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(subscription)
          });

          console.log('Backend’e abonelik iptali bildirildi.');
        } catch (backendErr) {
          console.error('Backend’e iptal bildirimi gönderilirken hata:', backendErr);
        }

      } else {
        console.warn('Abonelik iptal edilemedi.');
      }

    } catch (err) {
      console.error('Push aboneliğini iptal ederken hata oluştu:', err.name, err.message);
    }
  };

  return {
    subscribe,
    unsubscribe
  };
};
