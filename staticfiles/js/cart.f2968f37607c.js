var updateBtns = document.getElementsByClassName('update-cart')
var updateBtn = document.getElementsByClassName('ad-count')

for(var j = 0; j < updateBtns.length; j++){
	updateBtns[j].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		console.log('productId:', productId, 'action:', action)

		if(user === 'AnonymousUser'){
			userlogin()

		}else{
			updateUserOrder(productId, action)
		}
	})
}



for(var k = 0; k < updateBtn.length; k++){
	updateBtn[k].addEventListener('click', function(){
		var adId = this.dataset.product
		var action = this.dataset.action
		console.log('adId:', adId, 'action:', action)

		if(user === 'AnonymousUser'){
			updateadcount(adId, action)

		}else{
			updateUseradcount(adId, action)
		}
	})
}





function userlogin(){
	document.querySelector(".container2").style.display = "flex";
}


function updateUserOrder(productId, action){
	console.log('User is logged in ,Sending data')

	var url = 'update_item'

	fetch(url, {
		method:'POST',
		headers:{
			'Content-Type':'application/json',
			'X-CSRFToken':csrftoken,
		},
		body:JSON.stringify({'productId': productId, 'action':action})
	})

	.then((response) =>{
		return response.json()
	})

	.then((data) =>{
		console.log('data:', data)
		location.reload()
	})
}







function updateadcount(adId, action){
	console.log('User is not logged in ,Sending data')

	var url = 'update_adcount'

	fetch(url, {
		method:'POST',
		headers:{
			'Content-Type':'application/json',
			'X-CSRFToken':csrftoken,
		},
		body:JSON.stringify({'adId': adId, 'action':action})
	})

	.then((response) =>{
		return response.json()
	})

	.then((data) =>{
		console.log('data:', data)
		location.reload()
	})
}


function updateUseradcount(adId, action){
	console.log('User is logged in ,Sending data')

	var url = 'update_useradcount'

	fetch(url, {
		method:'POST',
		headers:{
			'Content-Type':'application/json',
			'X-CSRFToken':csrftoken,
		},
		body:JSON.stringify({'adId': adId, 'action':action})
	})

	.then((response) =>{
		return response.json()
	})

	.then((data) =>{
		console.log('data:', data)
		location.reload()
	})
}











  // let image = document.querySelector('#img');
  // image.addEventListener("click", function () {
  //   let inputValue = parseInt(document.querySelector('#gimper').value, 10);
  //   inputValue = isNaN(inputValue) ? 0 : inputValue;
  //   inputValue++;
  //   document.querySelector('#gimper').value = inputValue;
  // })