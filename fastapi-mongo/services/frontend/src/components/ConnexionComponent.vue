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
                    <!-- <ui-button :disabled="isDisabled" @click="open = true" raised>Log In</ui-button> -->
                    <ui-button :disabled="isDisabled" @click="logIn()" raised>Log In</ui-button>
                </ui-form-field>
                <ui-dialog v-model="open" scrollable @confirm="onConfirm" :escapeKey=false>
                    <ui-dialog-title>
                        Current mood
                    </ui-dialog-title>
                    <ui-dialog-content>
                        <ui-list>
                            <ui-item v-for="(item, index) in moodList" :key="index">{{ item }}</ui-item>
                        </ui-list>
                    </ui-dialog-content>
                    <ui-dialog-actions>
                        <template #default="{ buttonClass }">
                            <ui-button :class="buttonClass" acceptText @click="logIn()" raised>Confirm</ui-button>
                        </template>
                    </ui-dialog-actions>
                </ui-dialog>
            </template>
        </ui-form>
    </div>
</template>

<script>
import {store} from './../store.js'
import axios from 'axios'
axios.defaults.baseURL = 'http://0.0.0.0:5000/'
export default {
    data() {
        return {
            valueEmail: '',
            valuePassword: '',
            isDisabled: true,
            open: false,
            moodList: {1: "Happy", 2: "Sad", 3: "None"},
            accessTokenData: ''
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
        },
        onConfirm(result) {
            if (result) {
                console.log('ok')
            } else {
                console.log('cancel')
            }
        },
        redirectToHome() {
            this.$router.push('/accueil')
        },
        logIn() {
            this.accessTokenData = axios.post("/user/token/", {"email":this.valueEmail,"password":this.valuePassword})
                .then((response) => {
                    console.log(response.data.access_token)
                    store.set_access_token(response.data.access_token)
                    this.$router.push('/')
                })
                // .then((response) => {
                //     this.accessTokenData = response.data.access_token
                //     this.$router.push('/')
                // }, (error) => {
                //     console.log(error)
                // })
            console.log(this.accessTokenData)
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