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
            <h1 class="text-4xl font-bold text-center">Kayıt Ol</h1>
        </article>
        <form @submit.prevent="register" class="w-full">
            <label class="label">Adınız</label>
            <input v-model="first_name" type="text" class="input bg-base-200 border-b-gray-600 w-full" placeholder="Kullanıcı adınız" autocomplete="given-name" />

            <label class="label">Soyadınız</label>
            <input v-model="last_name" type="text" class="input bg-base-200 border-b-gray-600 w-full" placeholder="Kullanıcı adınız" autocomplete="family-name" />
            
            <label class="label">E-posta</label>
            <input v-model="email" type="email" class="input bg-base-200 border-b-gray-600 w-full" placeholder="Email" autocomplete="off" />

            <label class="label">Şifre</label>
            <input v-model="password" type="password" class="input bg-base-200 border-b-gray-600 w-full" placeholder="Password" autocomplete="new-password" />

            <button class="btn btn-primary w-full mt-4">
                Kayıt ol
            </button>
            <div class="py-5 sm:py-10 md:py-20">
                <div class="divider">Bir Hesabın mı Var ?</div>
            </div>
            <button type="button" class="btn btn-secondary text-white w-full mx-auto" @click="$router.push('/auth/login')">
                Giriş Yap
            </button> 
        </form>
    </div>
</section>
</template>

<script setup>
const accessToken = useCookie('access_token')
const refreshToken = useCookie('refresh_token')
const { $api } = useNuxtApp()
const toast = useToast()
const router = useRouter()

const first_name = ref('')
const last_name = ref('')
const email = ref('')
const password = ref('')

const register = async () => {
    try{
        const tokens = await $api('/auth/register',{
        method: 'POST',
            body: {
                first_name: first_name.value,
                last_name: last_name.value,
                email: email.value,
                password: password.value
            }
        })
        accessToken.value = tokens.access
        refreshToken.value = tokens.refresh
        toast.add({
            title:'Kayıt Başarılı',
            description: 'Giriş Sayfasına yönlendiriliyorsunuz, e-postanızı onaylamayı unutmayın'
        })
        router.push('/auth/login')
    } catch (e) {
        if (e.status === 406){
            toast.add({
                title: 'Kayıt Başarısız!',
                description: 'E-postanızı kontrol ediniz',
                color: 'red',
                icon: 'i-heroicons-exclamation-triangle'
            })
        }
    }
}
definePageMeta({
  layout: 'auth'
})
</script>