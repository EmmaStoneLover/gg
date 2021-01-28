
// console.log('Эта жопа работает');

new Vue({
	el: "#comments",
	delimiters: ['[[', ']]'],
	data: {
		cum_ena: true,
		cum: 2,
		cum_word: 'Комментарий',
	},
	methods: {

	},
	computed: {
		// if (cum > 0) {
		// 	cum_ena = true
		// }
	}
});
