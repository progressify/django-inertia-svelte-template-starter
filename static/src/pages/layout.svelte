<script>
  import { inertia } from '@inertiajs/inertia-svelte'
</script>

<!-- (A) SIDEBAR -->
<div id="pgside">
    <!-- (A1) BRANDING OR USER -->
    <!-- LINK TO DASHBOARD OR LOGOUT -->
    <div id="pguser">
        <img src="/static/img/potato.png">
        <i class="txt">MY ADMIN</i>
    </div>

    <!-- (A2) MENU ITEMS -->
    <a use:inertia href="/" class="current">
        <i class="ico">&#9733;</i>
        <i class="txt">Home</i>
    </a>
    <a use:inertia href="/about/">
        <i class="ico">&#9728;</i>
        <i class="txt">About us</i>
    </a>
    <a use:inertia href="/contacts">
        <i class="ico">&#9737;</i>
        <i class="txt">Contacts</i>
    </a>
</div>

<!-- (B) MAIN -->
<main id="pgmain">
    <slot />
</main>