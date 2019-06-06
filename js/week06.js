function resetForm() {
  document.getElementById("shoppingForm").reset();
}

function focusFirstName() {
  document.forms[0].elements[0].focus();
  document.getElementById("firstName").scrollIntoView();
}

function submitForm() {}

function validateCardNumber(number) {
  let re = new RegExp("\\d{4}-?\\d{4}-?\\d{4}-?\\d{4}");
  let warning = document.getElementById("card_warning");
  if (!re.test(number)) {
    warning.style.display = "block";
  } else {
    warning.style.display = "none";
  }
}
