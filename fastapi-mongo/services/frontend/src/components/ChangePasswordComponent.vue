<template>
<div>
    <div v-if="!modified" id="inscriptionTitle">
        <h2>Change password</h2>
    </div>
    <div id="inscriptionForm" v-if="!modified">
        
        <ui-form type="|" item-margin-bottom="16" action-align="center">
            <template #default="{ actionClass }">
                <ui-form-field>
                    <ui-textfield outlined id="verifiedpassword" v-model="valueTryPassword" input-type="password" required>
                        Last password
                    </ui-textfield>
                </ui-form-field>
                <ui-form-field>
                    <ui-textfield outlined id="newPassword" v-model="valueNewPassword1" input-type="password" pattern="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$" required>
                        New password
                    </ui-textfield>
                </ui-form-field>
                <ui-form-field>
                    <ui-textfield outlined id="secondPassword" v-model="valueNewPassword2" input-type="password" pattern="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$" required>
                        Confirm new password
                    </ui-textfield>
                </ui-form-field>
                <ui-form-field>
                    <ui-textfield-helper id="password-helper" visible>
                        Password must be at least 8 characters<br>long, at least 1 uppercase letter,<br> 1 lowercase letter<br> and 1 number
                    </ui-textfield-helper>
                </ui-form-field>
                <ui-form-field :class="actionClass">
                    <p hidden>{{ enableSubmit() }}</p>
                    <ui-button :disabled="isDisabled" @click="changePassword()" raised>Validate new password</ui-button>
                </ui-form-field>
            </template>
        </ui-form>
    </div>
    <div id="inscriptionForm" v-if="modified">
        <h2 id="inscriptionTitle">Password changed !</h2>
    </div>

</div>
</template>

<script>
import { store } from './../store.js'
import axios from 'axios'
axios.defaults.baseURL = 'http://0.0.0.0:5000/'
export default {
    data() {
        return {
            valueTryPassword: '',
            truePassword: '',
            valueNewPassword1: '',
            valueNewPassword2: '',
            isDisabled: true,
            modified : false,
            idUser : '62441cbacb2d9a19dde02394',
            userData: {},
            store
        }
    },
    mounted() {
        this.userData = this.getUserData()._id
    },
    methods: {
        checkLastPassword() {
            axios.get("/user/"+this.idUser)
            .then(response => (this.truePassword = response.data.password))
            return(this.truePassword == this.valueTryPassword)
        },
        checkSamePassword() {
            return this.valueNewPassword1 == this.valueNewPassword2
        },
        enableSubmit() {
            if (this.checkLastPassword() && this.checkSamePassword() && this.validatePassword() ) {
                this.isDisabled = false
            } else {
                this.isDisabled = true
            }
        },
        validatePassword() {
            if (/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$/.test(this.valueNewPassword1)) {
                return true
            } else {
                return false
            }
        },
        changePassword() {
        // reformat the payload from [{name: Age, value: 10}, ...] to {Age:10, ...}
            //axios.put("/user/", {"_id":this.idUser,"password":this.valueNewPassword1})
            this.modified = true
            //.then()
            //.catch(e => console.log(e))
        },
        getUserData() {
            this.current_access_token = store.get_access_token()
            this.current_user_data = axios.get('/user/users/me/', {
                params: {
                token: this.current_access_token
                }
            })
                .then((response) => {
                console.log(response.data)
                })
            console.log(this.current_user_data)
            return this.current_user_data
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