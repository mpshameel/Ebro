const signUppremiumButton = document.getElementById('signUppremium');

const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');



signUppremiumButton.addEventListener('click', () => {
	container.classList.add("right-panel-active2");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active2");
});


signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});




