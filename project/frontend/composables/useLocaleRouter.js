import { useRouter, useLocalePath } from '#imports'

export function useLocaleRouter() {
  const router = useRouter()
  const localePath = useLocalePath()

  function go(path) {
    router.push(localePath(path))
  }

  return { go }
}
