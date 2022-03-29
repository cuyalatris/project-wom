<template>
    <div id="inscriptionForm">
        <ui-form type="|" item-margin-bottom="16" action-align="center">
            <template #default="{ actionClass }">
                <ui-form-field>
                    <ui-textfield outlined input-type="email" required>
                        Email
                    </ui-textfield>
                </ui-form-field>
                <ui-form-field>
                    <ui-textfield input-type="email" required>
                        Confirmer l'email
                    </ui-textfield>
                </ui-form-field>
                <ui-form-field>
                    <ui-textfield outlined input-type="password" required pattern=".{8,}" helper-text-id="pw-validation-msg" :attrs="{autocomplete: 'current-password'}">
                        Password
                    </ui-textfield>
                    <ui-textfield-helper id="pw-validation-msg" visible>
                        Must be at least 8 characters long
                    </ui-textfield-helper>
                </ui-form-field>
                <ui-form-field :class="actionClass">
                    <ui-button raised>Submit</ui-button>
                    <ui-button outlined>Cancel</ui-button>
                </ui-form-field>
            </template>
        </ui-form>
    </div>
</template>

<script>

</script>

<style scoped lang="scss">
</style>