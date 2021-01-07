new Vue({
	el: "#app",
	data: {
		text: "Введите текст",
		bg_color: "bg-dark",
		text_color: "text-white",
	},
	methods: {
		Change_bg(bg){
			this.bg_color = bg
		},
		Change_text(text){
			this.text_color = text
		}
	}
});
