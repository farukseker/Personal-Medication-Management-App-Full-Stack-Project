/*
let heatMapBuffer: Array<{ x: number; y: number; timestamp: string; view: number }> = [];

const ticket_number = localStorage.getItem('ticket');

// Verileri toplu olarak gönderme fonksiyonu
const sendHeatMapData = async () => {

    if (heatMapBuffer.length > 0 && ticket_number) { // sessionId var ise gönder
        const config = useRuntimeConfig();
        const apiHost = config.public.API_HOST;
        // const apiHost = 'http://127.0.0.1:8000/api';

        try {
            await fetch(`${apiHost}/analytical/heatmap`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(heatMapBuffer),
            });
            heatMapBuffer = []; // Gönderilen verileri temizle
        } catch (error) {
            console.error('Veri gönderme başarısız:', error);
        }
    }
};

// Mouse hareketlerini dinleme ve verileri toplama
export default defineNuxtPlugin(async () => {
    // Eğer sessionId yoksa, backend'den al ve store'a kaydet
    document.addEventListener('mousemove', (event) => {
        if (ticket_number) { // sessionId varsa veriyi ekle
            heatMapBuffer.push({
                x: event.clientX,
                y: event.clientY,
                timestamp: new Date().toISOString(),
                view: parseInt(ticket_number),
            });
        }
    });

    // Verileri her 5 saniyede bir gönder
    setInterval(sendHeatMapData, 5000);
});
*/