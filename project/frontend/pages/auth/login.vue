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
                <h1 class="text-4xl font-bold text-center">{{ $t('auth.login') }}</h1>
            </article>
            <form @submit.prevent="login" class="w-full">
                <label class="label">{{ $t('auth.email') }}</label>
                <input v-model="email" type="email" required class="input w-full" :placeholder="$t('auth.email')" autocomplete="email" />

                <label class="label">{{ $t('auth.password') }}</label>
                <input v-model="password" type="password" required class="input w-full" :placeholder="$t('auth.password')" autocomplete="current-password" />

                <div class="flex py-2 gap-2">
                    <input type="checkbox" name="pw" id="pwf" v-model="rember_me" class="checkbox checkbox-sm checkbox-primary my-auto" checked>
                    <label class="label my-auto" for="pwf">{{ $t('auth.rember_me') }}</label>
                </div>
                <button type="submit" class="btn btn-primary w-full">
                    {{ $t('auth.be_login') }}
                </button>
                <div class="py-10 md:py-20">
                    <div class="divider">{{ $t('auth.forget_password') }}</div>
                </div>
                <div class="flex flex-col gap-4">
                    <button type="button" class="btn btn-secondary text-white w-full mx-auto" @click="go('/auth/register')">
                        {{ $t('auth.register') }}
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
import { useI18n } from 'vue-i18n'
import { useLocaleRouter } from '~/composables/useLocaleRouter'

const { t } = useI18n()
const { go } = useLocaleRouter()
const { $api } = useNuxtApp()
const toast = useToast()

const email = ref('')
const password = ref('')
const rember_me = ref(true)

const login = async () => {
    try{
        const tokens = await $api('/auth/token/',{
        method: 'POST',
            body: {
                email: email.value,
                password: password.value
            }
        })
        
        const token_options = !rember_me.value ? {}:{
            maxAge: 60 * 60 * 24 * 30 * 6, // 6 ay mesela
            sameSite: 'lax',
            //secure:  true,
            path:    '/',
        }
        const accessToken = useCookie('access_token', token_options)
        const refreshToken = useCookie('refresh_token', token_options)
        accessToken.value = tokens.access
        refreshToken.value = tokens.refresh
        toast.add({
            title: t('auth.login_message_title'),
            description: t('auth.login_message_description')
        })
        go('/')
    } catch (e) {
console.log(e)
    }
}
definePageMeta({
  layout: 'auth'
})
</script>