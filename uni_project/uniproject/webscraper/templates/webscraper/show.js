(function(){
'use strict';

angular.module('webscraper', [])
.controller('WebscraperController', ['$scope', WebscraperController]);

function WebscraperController($scope) {
	$scope.add = function (list, title){
		var card = {
			title: title
		};

		list.cards.push(card);
	};

	$scope.data = [
	{
		name: 'Django demo',
		cards: [
		{
			title: 'Create Models'
		},
		{
			title: 'Create View'
		},
		{
			title: 'Migrate Database'
		},
		]
	},

{
	name: 'Angular demo',
	cards: [
	{
		title:'Write HTML'
	},
	{
		title: 'write JavaScript'
	},
	]
}
];
}
}());



// <!-- 			// alert("lol");

// 			// (function(){

// 			// 	'use strict';





// 			// 	angular.module('webscraper', [])
// 			// 	.controller('WebscraperController', ['$scope', WebscraperController]);

// 			// 		$http.post('http://localhost:5050/subscribe/?user=tomfriend89@googlemail.com&band=rise_against')
// 			// 			.then(
// 			// 		alert("yay"), alert("bollox")
// 			// 		);
// 			// 	function WebscraperController($scope, $http) {
// 			// 		$scope.add = function (list, title){
// 			// 			var card = {
// 			// 				title: title
// 			// 			};








// 			// 			list.cards.push(card);
						
// 			// 		};

// 			// 		$scope.data = [
// 			// 		{
// 			// 			name: 'Django demo',
// 			// 			cards: [
// 			// 			{
// 			// 				title: 'Create Models'
// 			// 			},
// 			// 			{
// 			// 				title: 'Create View'
// 			// 			},
// 			// 			{
// 			// 				title: 'Migrate Database'
// 			// 			},
// 			// 			]
// 			// 		},
				
// 			// 	{
// 			// 		name: 'Angular demo',
// 			// 		cards: [
// 			// 		{
// 			// 			title:'Write HTML'
// 			// 		},
// 			// 		{
// 			// 			title: 'write JavaScript'
// 			// 		},
// 			// 		]
// 			// 	}
// 			// 	];
// 			// }
// 			// }());

// 			// continue working on the plural sight getting angular JS working so you can save following an artist to the DB and look into how the session is stored as you need to be able to identify which user is accessing the website.



// 		</script> -->