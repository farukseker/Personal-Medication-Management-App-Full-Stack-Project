<template>
  <div class="p-4 space-y-4 max-w-md mx-auto">
    <!-- Navbar -->
    <div class="flex justify-between items-center">
      <h1 class="text-xl font-bold">İlaç Takibi</h1>
      <button class="btn btn-ghost btn-sm">
        <i class="i-lucide-settings text-xl"></i>
      </button>
    </div>

    <!-- Günün Planı -->
    <div>
      <h2 class="text-lg font-semibold mb-2">Bugün, 13 Mayıs</h2>
      <div class="space-y-3">
        <div class="card bg-base-100 shadow-sm">
          <div class="card-body p-3">
            <div class="flex justify-between items-center">
              <div>
                <p class="font-semibold">Parol 500mg</p>
                <p class="text-sm text-gray-500">Saat 14:00 - 1 tablet</p>
              </div>
              <div class="flex gap-2">
                <button class="btn btn-success btn-sm">Aldım</button>
                <button class="btn btn-outline btn-sm">Atla</button>
              </div>
            </div>
          </div>
        </div>
        <!-- Diğer ilaç kartları da aynı şekilde -->
      </div>
    </div>

    <!-- Haftalık Durum -->
    <div class="card bg-base-100 shadow-md">
      <div class="card-body">
        <h3 class="text-md font-medium">Bu hafta</h3>
        <progress class="progress progress-primary w-full" value="60" max="100"></progress>
        <p class="text-sm text-gray-500 mt-1">6 / 10 doz alındı</p>
      </div>
    </div>

    <!-- Hızlı Aksiyonlar -->
    <div class="grid grid-cols-3 gap-2">
      <button class="btn btn-primary btn-sm">+ İlaç Ekle</button>
      <button class="btn btn-outline btn-sm">📈 Geçmiş</button>
      <button class="btn btn-outline btn-sm">👨‍⚕️ Paylaş</button>
    </div>
  </div>
</template>
