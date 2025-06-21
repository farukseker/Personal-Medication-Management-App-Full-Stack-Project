<template>
<section class="px-4 space-y-4 max-w-md mx-auto">
    <header>
        <button class="btn btn-ghost ps-0 text-xl">
            <font-awesome :icon="faArrowLeft" />
        </button>
        <h1 class="text-xl font-bold">Ayarlar</h1>
    </header>
    <article>

    <form>
        <fieldset class="w-full fieldset border-b-2 shadow card border-base-300 rounded-box p-4 gap-4">
            <legend class="fieldset-legend font-bold">Şifre değiştir</legend>
            <label>
                <span>Eski Şifreniz</span>
                <font-awesome :icon="faCircle" class="scale-50 mx-1 text-gray-200" />
                <a>Şifrenizi mi unuttunuz ?</a>
            </label>
            <input v-model="newPasswordFormData.current_password" class="input w-full" type="password" autocomplete="password" placeholder="Şifreniz">
            <label>Yeni Şifreniz</label>
            <input v-model="newPasswordFormData.new_password" class="input w-full" type="password" autocomplete="new-password" placeholder="Yeni Şifreniz">
            <label>Yeni Şifreniz'i tekrar girin</label>
            <input v-model="newPasswordFormData.new_password_repeat" class="input w-full" type="password" autocomplete="new-password" placeholder="Yeni Şifreniz">
            <div class="space-y-2 mt-4">
                <div v-for="(passed, key) in passwordRules" :key="key" class="flex items-center gap-2">
                <span
                    :class="passed ? 'text-green-500' : 'text-red-500'"
                    class="text-lg"
                >
                    <font-awesome :icon="passed ? faCheckCircle : faTimesCircle" />
                </span>
                <span :class="passed ? 'text-green-600' : 'text-red-600'">
                    {{ ruleTexts[key] }}
                </span>
                </div>
            </div>
            <div class="w-full flex">
                <div class="w-full"></div>
                <button class="btn btn-primary w-fit" :disabled="passwordCorrect">Kaydet</button>
            </div>
      </fieldset>
    </form>
    </article>
</section>
</template>

<script setup>
import { faCheckCircle, faTimesCircle } from '@fortawesome/free-solid-svg-icons'

const passwordRules = ref({
  minLength: false,
  specialChar: false,
  repeatMatch: false,
  commonPassword: true,
  onlyNumbers: false,
  notSimilarToUser: true
})

const ruleTexts = {
  minLength: 'En az 8 karakter',
  specialChar: 'En az 1 özel karakter (!@#...)',
  repeatMatch: 'Şifreler aynı',
  commonPassword: 'Çok yaygın bir şifre değil',
  onlyNumbers: 'Sadece rakamdan oluşmuyor',
  notSimilarToUser: 'Adın ya da e-postanla benzer değil'
}

// Örnek form datası
const newPasswordFormData = ref({
  current_password: '',
  new_password: '',
  new_password_repeat: ''
})

// Validasyon fonksiyonu
const validateNewPassword = (password, repeat, username = '', email = '') => {
  passwordRules.value.minLength = password.length >= 8
  passwordRules.value.specialChar = /[!@#$%^&*()_+{}\[\]:;<>,.?~\\\-]/.test(password)
  passwordRules.value.repeatMatch = password === repeat
  passwordRules.value.commonPassword = ![
    '123456', 'password', '12345678', 'qwerty', 'abc123',
    '111111', '123123', '000000', 'iloveyou', '1234'
  ].includes(password.toLowerCase())
  passwordRules.value.onlyNumbers = !/^\d+$/.test(password)
  passwordRules.value.notSimilarToUser =
    !(username && password.toLowerCase().includes(username.toLowerCase())) &&
    !(email && password.toLowerCase().includes(email.toLowerCase()))
}

// Watch ile tetikle
watch(newPasswordFormData, (newData) => {
  const username = 'pars'
  const email = 'pars@example.com'
  validateNewPassword(newData.new_password, newData.new_password_repeat, username, email)
}, { deep: true })
</script>