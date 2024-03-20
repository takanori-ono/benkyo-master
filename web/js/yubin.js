
const contactForm = document.forms.contactForm;
// console.log(contactForm)
// const post_code = contactForm.postcode.value
// contactForm.postcode.value=1234
contactForm.postcode.addEventListener('input', e => {
  const post_code = e.target.value
  if(post_code.length === 7) {
    const query = `https://zipcloud.ibsnet.co.jp/api/search?zipcode=${post_code}`
    // console.log(query)
    fetch(query)
    .then(r => r.json())
    .then(d => {
      if(d.results){
        const a = d.results[0];
        // console.log(a)
        contactForm.prefecture.value = a.address1;
        contactForm.city.value = a.address2;
        contactForm.town.value = a.address3;
      }
    })
    .catch(e => alert(e))
  }
})
