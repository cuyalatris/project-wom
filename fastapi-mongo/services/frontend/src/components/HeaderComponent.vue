<template>
    <div>
        <ui-grid>
            <ui-grid-cell id="headerCellTitle">
                <h1>WatchOurMovie</h1>
            </ui-grid-cell>
            <ui-grid-cell id="headerCellSearchBar">
                <ui-textfield id="searchBar" v-model="searchBarInput" :source="moviesList" placeholder="Search for a movie"></ui-textfield>
            </ui-grid-cell>
            <ui-grid-cell class="heacerCell"></ui-grid-cell>
        </ui-grid>
    </div>
</template>

<script>
export default {
    data() {
        return {
            searchBarInput: '',
            moviesList: ["Movie1","Movie2","Movie3","Movie4","Movie5","Movie6","Movie7"]
        }
    }
}
</script>

<style scoped lang="scss">
    div {
        padding: 10px;
        color: #fff;
        background-color: #2c3e50
    }
</style>