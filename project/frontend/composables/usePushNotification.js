export const usePushNotification = () => {
  const vapidPublicKey = "BPDBH_bt8haJg_WEhwH7ppGUV2zDEGyoQkcGDD_rkPkG-6y-KoGSf9biaR_-sCxlK2BDgXiQDFR3mSmhePMsfPU"; // sunucudan al

  const urlBase64ToUint8Array = (base64String) => {
    const padding = '='.repeat((4 - base64String.length % 4) % 4);
    const base64 = (base64String + padding)
      .replace(/-/g, '+')
      .replace(/_/g, '/');

    const rawData = atob(base64);
    const outputArray = new Uint8Array(rawData.length);

    for (let i = 0; i < rawData.length; ++i) {
      outputArray[i] = rawData.charCodeAt(i);
    }
    return outputArray;
  };

  const subscribe = async () => {
    if (!('serviceWorker' in navigator)) {
      console.warn('Tarayıcı service worker desteklemiyor.');
      return;
    }

    const permission = await Notification.requestPermission();
    if (permission !== 'granted') {
      console.warn('Kullanıcı bildirim izni vermedi.');
      return;
    }
    console.log('Push aboneliği:', urlBase64ToUint8Array(vapidPublicKey));

    const registration = await navigator.serviceWorker.register('/sw.js');
    const subscription = await registration.pushManager.subscribe({
      userVisibleOnly: true,
      applicationServerKey: urlBase64ToUint8Array(vapidPublicKey)
    });

    console.log('Push aboneliği:', subscription);

    // Backend'e POST et
    await $fetch('/api/medication/subscribe/', {
      method: 'POST',
      body: subscription
    });

    console.log('Abonelik backend\'e gönderildi.');
  };

  return {
    subscribe
  };
};
