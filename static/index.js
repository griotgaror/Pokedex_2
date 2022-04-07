
var MAIN = {};
MAIN.init = function() {
	const POKEMON_CONTAINER = document.querySelectorAll(".pokemon_container");

	//spin card to the back or front side
	POKEMON_CONTAINER.forEach(container => {
		container.onclick = function() {

			let back_side = "rotateY(90deg)";
			let front_side = "rotateY(0deg)";

			container.style.transform = (container.style.transform == front_side) ? back_side : front_side;  
		};
	});

	//search pokemon
	const SEARCHBAR = document.getElementById("searchbar");

	SEARCHBAR.oninput = () => {
		POKEMON_CONTAINER.forEach(container => {

			let user_input = SEARCHBAR.value;
			let pokename = container.id;

			if (pokename.charAt(0) != user_input.charAt(0)) {
				//show all pokemon it's the input none
				container.style.display = (user_input) ? "none" : "flex";
			} else {
				//filter pokemon from user_input
				for (let i = 1; i < user_input.length; i++) {
					container.style.display = (pokename.charAt(i) == user_input.charAt(i)) ? "flex" : "none";
				};
			};
		});
	};
};


window.onload = MAIN.init();