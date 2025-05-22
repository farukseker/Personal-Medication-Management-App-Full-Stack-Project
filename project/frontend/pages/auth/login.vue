<template>
    <section class="
        w-full min-h-screen mt-5 md:mt-0 md:flex justify-center
        bg-gradient-to-t 
        from-base-300 to-base-100
        text-xl
        ">
        <div class="m-auto w-full sm:w-8/12 lg:w-4/12 px-4">
            <article class="w-fit mx-auto">
                <img src="/pill.svg" alt="">
                <h1 class="text-4xl font-bold text-center">Giriş</h1>
            </article>
            <form @submit.prevent="login" class="w-full">
                <label class="label">E-posta</label>
                <input v-model="email" type="email" required class="input w-full" placeholder="Email" />

                <label class="label">Şifre</label>
                <input v-model="password" type="password" required class="input w-full" placeholder="Password" />

                <div class="flex">
                    <input type="checkbox" name="pw" id="pwf">
                    <label class="label" for="pwf">Şifremi unuttum</label>
                </div>
                <button type="submit" class="btn btn-primary w-full">
                    Giriş yap
                </button>
                <div class="py-20">

                </div>
                <button type="button" class="btn btn-warning text-white w-full mx-auto">
                    Google ile giriş
                </button> 
            </form>
        </div>
    </section>
</template>
<script setup>
const accessToken = useCookie('access_token', {
    maxAge: 60 * 60 * 24 * 30,
    sameSite: 'lax',   // CSRF dostu
    secure:  true,     // prod’da HTTPS şart
    path:    '/',      // tüm route'larda erişilsin
})
const refreshToken = useCookie('refresh_token',{
    maxAge: 60 * 60 * 24 * 30 * 6, // 6 ay mesela
    sameSite: 'lax',
    secure:  true,
    path:    '/',
})


const { $api } = useNuxtApp()
const toast = useToast()
const router = useRouter()

const email = ref('')
const password = ref('')

const login = async () => {
    try{
        const tokens = await $api('/auth/token/',{
        method: 'POST',
            body: {
                email: email.value,
                password: password.value
            }
        })
        accessToken.value = tokens.access
        refreshToken.value = tokens.refresh
        toast.add({
            title:'Giriş Yapıldı',
            description: 'Ana sayfaya yönlendirliyorusunz'
        })
        router.push('/')
    } catch {

    }
}
definePageMeta({
  layout: 'auth'
})
</script>