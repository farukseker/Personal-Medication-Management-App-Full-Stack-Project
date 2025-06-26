<template>
  <section class="px-4 space-y-6 max-w-md mx-auto">
    <!-- Header -->
    <header class="flex items-center">
      <button class="btn btn-ghost ps-0 text-xl z-10" @click="go('/settings')">
        <font-awesome :icon="faArrowLeft" />
      </button>
      <h1 class="text-xl font-bold w-full text-center -ms-8">Kişisel</h1>
    </header>

    <!-- Profil Fotoğrafı (Tıklanabilir) -->
    <div class="flex justify-center">
      <label for="file-upload" class="cursor-pointer">
        <div class="avatar">
          <div class="w-24 rounded-full ring ring-primary ring-offset-base-100 ring-offset-2 hover:opacity-80 transition-all">
            <img :src="previewImage || user.profile_picture || '/pp.jpg'" alt="Profil Fotoğrafı" />
          </div>
        </div>
        <input
          id="file-upload"
          type="file"
          accept="image/*"
          class="hidden"
          @change="onFileChange"
        />
      </label>
    </div>

    <!-- Ad Soyad -->
    <div class="space-y-4">
      <div class="form-control">
        <label class="label">
          <span class="label-text font-semibold">
            <font-awesome :icon="faUser" class="me-2" />Ad
          </span>
        </label>
        <input
          type="text"
          class="input input-bordered w-full"
          v-model="user.first_name"
          placeholder="Adınızı girin"
        />
      </div>

      <div class="form-control">
        <label class="label">
          <span class="label-text font-semibold">
            <font-awesome :icon="faUser" class="me-2" />Soyad
          </span>
        </label>
        <input
          type="text"
          class="input input-bordered w-full"
          v-model="user.last_name"
          placeholder="Soyadınızı girin"
        />
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import { faArrowLeft, faUser } from '@fortawesome/free-solid-svg-icons'
import { useLocaleRouter } from '~/composables/useLocaleRouter'
import { useUserStore } from '~/stores/user_store'

const { go } = useLocaleRouter()
const userStore = useUserStore()

// Kullanıcı bilgileri
const user = ref({
  profile_picture: userStore.profile_picture,
  first_name: userStore.first_name,
  last_name: userStore.last_name
})

const previewImage = ref(null)

function onFileChange(event) {
  const file = event.target.files[0]
  if (!file) return

  const reader = new FileReader()
  reader.onload = () => {
    previewImage.value = reader.result

    // Örneğin: Store'u da güncelle (ya da API'ye yolla)
    userStore.profile_picture = reader.result
  }
  reader.readAsDataURL(file)
}
</script>
