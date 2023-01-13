<script>
    import { page } from '@inertiajs/inertia-svelte'
</script>

> {$page.props.page_name}

<ul>
{#each $page.props.events as event}
	<li>{event}</li>
{/each}
</ul>

