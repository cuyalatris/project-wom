<template>
    <div id="connexionTitle">
        <h2>Log In</h2>
    </div>
    <div id="connexionForm">
        <ui-form type="|" item-margin-bottom="16" action-align="center">
            <template #default="{ actionClass }">
                <ui-form-field>
                    <ui-textfield outlined id="email" v-model="valueEmail" input-type="email" required>
                        Email
                    </ui-textfield>
                </ui-form-field>
                <ui-form-field>
                    <ui-textfield outlined id="password" v-model="valuePassword" input-type="password" required>
                        Password
                    </ui-textfield>
                </ui-form-field>
                <ui-form-field :class="actionClass">
                    <p hidden>{{ enableSubmit() }}</p>
                    <ui-button :disabled="isDisabled" raised>Log In</ui-button>
                </ui-form-field>
            </template>
        </ui-form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            valueEmail: '',
            valuePassword: '',
            isDisabled: true
        }
    },
    methods: {
        validateEmail() {
            if (/^(([^<>()\]\\.,;:\s@"]+(\.[^<>()\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,24}))$/.test(this.valueEmail)) {
                return true
            } else {
                return false
            }
        },
        enableSubmit() {
            if (this.validateEmail()) {
                this.isDisabled = false
            } else {
                this.isDisabled = true
            }
        }
    }
}
</script>

<style scoped lang="scss">
#connexionTitle {
    display: flex;
    align-items: center;
    justify-content: center;
}
#connexionForm {
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>