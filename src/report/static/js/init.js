const app = Vue.createApp({
  delimiters: ['[[', ']]'],
  data() {
    return {
      nationalReport: [],
      authorityContact: [],
      regionInfo: [],
    }
  },
  methods: {
    retrieveNationalReports() {
      axios.get('/api/national-report/')
        .then(response => {
          this.nationalReport = response.data;
          console.log(response.data);
          // toast({ html: 'Network Connected!', classes: 'teal darken-4' });
        })
        .catch(e => {
          console.log(e);
          // toast({ html: 'Network Error!', classes: 'red darken-4' });
        });
    },
    getAuthorityContact() {
      axios.get('/api/public-authority/')
        .then(response => {
          this.authorityContact = response.data;
          console.log(response.data);
          // M.toast({ html: 'Network Connected!', classes: 'teal darken-4' });
        })
        .catch(e => {
          console.log(e);
          // M.toast({ html: 'Network Error!', classes: 'red darken-4' });
        });
    },
    getRegion(){
      axios.get('api/region/')
        .then(response => {
          this.regionInfo = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },
  },
  mounted() {
    // AutoInit();
    this.retrieveNationalReports();
    this.getAuthorityContact();
    this.getRegion();
  },
})

app.mount('#app')