<template>
  <div id="login" class="flex flex-col items-center h-full">
    <h1
      class="animated zoomInDown user-form-title text-6xl tracking-wide text-orange-600 mt-10 mb-10"
    >Login!</h1>
    <div class="form-wrapper h-64 w-2/4 flex">
      <form
        class="flex flex-col w-full justify-around p-40 text-gray-900"
        @submit.prevent="handleSubmit"
      >
        <label>Email</label>
        <input
          placeholder=" email"
          name="email"
          v-model="data.email"
          type="text"
          required="required"
        />
        <label>Password</label>
        <input
          placeholder=" password"
          name="password"
          v-model="data.password"
          type="password"
          required="required"
        />
        <label>Confirm your password</label>
        <input
          placeholder=" password confirmation"
          name="password_confirmation"
          v-model="data.password_confirmation"
          type="password"
          required="required"
        />
        <button type="submit" class="form-button mt-5">Submit</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Auth from "../../lib/auth";
import { eventBus } from "../../main";

export default {
  name: "login",
  data() {
    return {
      data: {}
    };
  },

  methods: {
    async handleSubmit() {
      try {
        const res = await axios.post("/api/login", this.data);
        Auth.setToken(res.data.token);
        this.$router.push("/profile");
        // eventBus.$emit('userLoggedIn')
        // use the method set up in the event bus in app.js which emits the event of the user logging in
        eventBus.loginCheck();
      } catch (err) {
        this.$router.push("/notfound");
      }
    }
  }
};
</script>
<style scoped></style>
