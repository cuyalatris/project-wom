<template>
    <div id="inscriptionTitle">
        <h2>Sign In</h2>
    </div>
    <div id="inscriptionForm">
        <ui-form type="|" item-margin-bottom="16" action-align="center">
            <template #default="{ actionClass }">
                <ui-form-field>
                    <ui-textfield outlined id="username" v-model="valueUsername" input-type="text" pattern=".{4,}" required>
                        Username
                    </ui-textfield>
                </ui-form-field>
                <ui-form-field>
                    <ui-textfield outlined id="firstEmail" v-model="valueEmail1" input-type="email" required>
                        Email
                    </ui-textfield>
                </ui-form-field>
                <ui-form-field>
                    <ui-textfield outlined id="secondEmail" v-model="valueEmail2" input-type="email" required>
                        Confirm email
                    </ui-textfield>
                </ui-form-field>
                <ui-form-field>
                    <ui-textfield outlined id="firstPassword" v-model="valuePassword1" input-type="password" pattern="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$" required>
                        Password
                    </ui-textfield>
                </ui-form-field>
                <ui-form-field>
                    <ui-textfield outlined id="secondPassword" v-model="valuePassword2" input-type="password" pattern="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$" required>
                        Confirm password
                    </ui-textfield>
                </ui-form-field>
                <ui-form-field>
                    <ui-textfield-helper id="password-helper" visible>
                        Password must be at least 8 characters<br>long, at least 1 uppercase letter,<br> 1 lowercase letter<br> and 1 number
                    </ui-textfield-helper>
                </ui-form-field>
                <ui-form-field :class="actionClass">
                    <p hidden>{{ enableSubmit() }}</p>
                    <ui-button :disabled="isDisabled" @click="SignIn()" raised>Sign In</ui-button>
                </ui-form-field>
            </template>
        </ui-form>
    </div>
</template>

<script>
import axios from 'axios'
axios.defaults.baseURL = 'http://0.0.0.0:5000/'
export default {
    data() {
        return {
            valueEmail1: '',
            valueEmail2: '',
            valuePassword1: '',
            valuePassword2: '',
            isDisabled: true,
            form:''
        }
    },
    methods: {
        checkSameEmail() {
            return (this.validateEmail() && this.valueEmail1 == this.valueEmail2)
        },
        checkSamePassword() {
            return this.valuePassword1 == this.valuePassword2
        },
        enableSubmit() {
            if (this.checkSameEmail() && this.checkSamePassword()) {
                this.isDisabled = false
            } else {
                this.isDisabled = true
            }
        },
        validateEmail() {
            if (/^(([^<>()\]\\.,;:\s@"]+(\.[^<>()\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,24}))$/.test(this.valueEmail1)) {
                return true
            } else {
                return false
            }
        },
        validatePassword() {
            if (/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$/.test(this.valuePassword1)) {
                return true
            } else {
                return false
            }
        },
        SignIn() {
        // reformat the payload from [{name: Age, value: 10}, ...] to {Age:10, ...}
            axios.post("/user/", {"userName":this.valueUsername,"email":this.valueEmail1, "password":this.valuePassword1})
            //.then()
            //.catch(e => console.log(e))
        }

    }
}
</script>

<style scoped lang="scss">
#inscriptionTitle {
    display: flex;
    align-items: center;
    justify-content: center;
}
#inscriptionForm {
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>