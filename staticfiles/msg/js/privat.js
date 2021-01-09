


new Vue({
	el: "#app",
	delimiters: ['[[', ']]'],
	data: {
		text: "Введите текст",
		bg_color: "bg-dark",
		text_color: "text-white",
		smth: JSON.parse(document.getElementById('smth').textContent),
	},
	methods: {
		Change_bg(bg){
			this.bg_color = bg
		},
		Change_text(text){
			this.text_color = text
		}
	},
	computed: {
		smthing: function () {
			if (this.bg_color == "bg-success")
			  return "Ура бля!"
			else
				return this.smth
    }
	}
});
