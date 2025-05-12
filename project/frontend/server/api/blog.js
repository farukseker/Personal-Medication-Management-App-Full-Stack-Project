let cachedBlogs = null;
let lastFetchTime = null;

export default defineEventHandler(async (event) => {
  console.log('API route hit');  // Bu log, API route'una her istek geldiğinde görünmeli

  const now = new Date();  // Correctly initialized before use


  // Eğer verinin cache süresi dolmadıysa, cached veriyi döndür
  if (cachedBlogs && lastFetchTime && (now - lastFetchTime) < 3600000) {
    console.log('Cache hit');
    return cachedBlogs;  // Cache'deki veriyi döndürüyoruz
  }

  // Cache süresi dolmuşsa yeni veriyi çek
  try {
    console.log('Fetching new data from external API');
    const response = await fetch('https://api.farukseker.com.tr/api/content/all/blog');
    const data = await response.json();
    console.log('Data fetched:', data);  // Veriyi terminalde görmek için log ekleyin
    cachedBlogs = data;
    lastFetchTime = now;
    return data;  // Yeni veriyi döndürüyoruz
  } catch (error) {
    console.error('Veri çekme hatası:', error);
    return { error: 'Veri çekme hatası' };  // Hata durumunda mesaj döndürüyoruz
  }
});
