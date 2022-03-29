<template>
    <div id="connexionForm">
        <h2>Connexion</h2>
        <form id="connexion">
            <input v-model="text" placeholder="Identifiant" required>
            <br>
            <input v-model="password" placeholder="Mot de passe" required>
            <br>
            <button type="submit">Se connecter</button>
        </form>
    </div>
</template>

<script>

</script>

<style scoped lang="scss">
</style>