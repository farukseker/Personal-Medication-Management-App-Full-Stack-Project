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
                <input v-model="email" type="email" required class="input w-full" placeholder="Email" autocomplete="email" />

                <label class="label">Şifre</label>
                <input v-model="password" type="password" required class="input w-full" placeholder="Password" autocomplete="current-password" />

                <div class="flex py-2 gap-2">
                    <input type="checkbox" name="pw" id="pwf" class="checkbox checkbox-sm checkbox-primary my-auto" checked>
                    <label class="label my-auto" for="pwf">Beni Hatırla</label>
                </div>
                <button type="submit" class="btn btn-primary w-full">
                    Giriş yap
                </button>
                <div class="py-10 md:py-20">
                    <div class="divider">Şifremi unuttum</div>
                </div>
                <div class="flex flex-col gap-4">
                    <button type="button" class="btn btn-secondary text-white w-full mx-auto" @click="$router.push('/auth/register')">
                        Kayıt ol
                    </button> 
                    <div class="flex gap-8 justify-center">
                        <button type="button" class="btn btn-outline">
                            <font-awesome :icon="faGoogle" />
                        </button>
                        <button type="button" class="btn btn-outline">
                            <font-awesome :icon="faMeta" />
                        </button>
                        <button type="button" class="btn btn-outline">
                            <font-awesome :icon="faGithub" />
                        </button>
                    </div>
                </div>
            </form>
        </div>
    </section>
</template>
<script setup>
import { faGoogle, faMeta, faGithub } from '@fortawesome/free-brands-svg-icons'

const accessToken = useCookie('access_token')
const refreshToken = useCookie('refresh_token')


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