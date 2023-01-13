import { createInertiaApp } from '@inertiajs/inertia-svelte'
import { InertiaProgress } from '@inertiajs/progress'
import Layout from '../pages/layout.svelte'

InertiaProgress.init();

createInertiaApp({
  resolve: async (name) => {
    const comps = import.meta.glob('../pages/**/*.svelte');
    const match = comps[`../pages/${name}.svelte`];
    const page = (await match());

    return Object.assign({layout: Layout}, page);
  },
  setup({ el, App, props }) {
    new App({ target: el, props })
  },
});
