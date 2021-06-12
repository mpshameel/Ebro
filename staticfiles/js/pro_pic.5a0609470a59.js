
// declairing html elements

// const imgDiv = document.querySelector('.profile-pic-div');
// const img = document.querySelector('#photo');
// const file = document.querySelector('#file');
// const uploadBtn = document.querySelector('#uploadBtn');

// if user hover on profile pic
// imgDiv.addEventListner('mouseenter', function()
// {
// 	uploadBtn.style.display = "block";
// });

// // if user hover out from profile pic
// imgDiv.addEventListner('mouseleave', function()
// {
// 	uploadBtn.style.display = "none"
// });


// //image showing functionality
// //when we choose a a photo to upload
// file.addEventListner('change', function(){
// 	//this refer to file
// 	const choosedFile = this.files[0];
// 	if (choosedFile) {
// 		const reader = new FileReader();//filereader is a predefined function of js
// 		reader.addEventListner('load', function(){
// 			img.setAttribute('src', reader.result);
// 		});

// 		reader.readAsDataURL(choosedFile);
// 	}
// });




function showPreview(event){
	if(event.target.files.length > 0){
		var src = URL.createObjectURL(event.target.files[0]);
		var preview = document.getElementById("file-ip-1-preview");
		preview.src = src;
		preview.style.display = "block";
	}
}




