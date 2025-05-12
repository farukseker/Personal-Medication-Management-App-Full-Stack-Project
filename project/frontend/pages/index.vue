<template>
  <div class="flex flex-col gap-4 bg-gradient-to-t from-base-300 to-base-100">
    <UsersUserHeader class="sticky top-0 left-0" />
    <NavNavigationShortcut />
    
    <section class="flex flex-col gap-4 px-2 md:px-4 min-h-screen">
      <FormsMedicineHistoryForm />
      <article class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <MedicationUseHistory />
        <MedicationNextHistory />
      </article>
    </section>
</div>
</template>
  
<script setup>
import { useMyMedicationStore } from '@/stores/my_medication_store.js'
import { NavNavigationShortcut } from '#components'

const my_medication_store = useMyMedicationStore()
onMounted(my_medication_store.getMedicationList)

useSeoMeta({
      title: 'İlaç Takip',
      ogTitle: 'İlaç Takip',
      description: 'İlaçlarını takip et sağlık durumunu kolayca raporla',
      ogDescription: 'İlaçlarını takip et sağlık durumunu kolayca raporla',
      ogImage: 'https://res.cloudinary.com/dlusw5ukg/image/upload/v1738064760/portfolyo/static/img/faruk2_buutol.jpg',
      twitterCard: 'summary_large_image',
      author: 'F4ruk-Seker'
})
</script>
