<template>
<section class="
    w-full min-h-screen mt-5 md:mt-0 md:flex justify-center
    bg-gradient-to-t 
    from-base-300 to-base-100
    text-xl
    ">
    <div class="my-auto w-full sm:w-8/12 md:w-4/12 px-4">
        <article class="w-fit mx-auto">
            <img src="/pill.svg" alt="">
            <h1 class="text-4xl font-bold text-center">Kayıt Ol</h1>
        </article>
        <article class="w-full">
            <label class="label">Rumuz</label>
            <input type="text" class="input w-full" placeholder="Kullanıcı adınız" />

            <label class="label">E-posta</label>
            <input type="email" class="input w-full" placeholder="Email" />

            <label class="label">Şifre</label>
            <input type="password" class="input w-full" placeholder="Password" />

            <button class="btn btn-primary w-full">
                Giriş yap
            </button>
        </article>
        <article class="bottom-5 sm:bottom-10 md:bottom-20 w-full left-0 px-4 md:px-8 absolute flex">
            <button class="btn btn-warning text-white w-full sm:w-8/12 md:w-4/12 mx-auto">
                Google ile giriş
            </button> 
        </article>
    </div>
</section>
</template>