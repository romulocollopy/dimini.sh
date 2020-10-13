(function(){
  const ERROR_MESSAGE = "Sory, something whent wrong... \n\n";

  class Page{
    constructor(body){
      this.form = body.querySelector("form");
      this.result_box = body.querySelector("div.result");
      this.result_text = this.result_box.querySelector("#shortened");
      this.error_text = this.result_box.querySelector("#error");
      this.init_form();
    }

    init_form(){
      this.form.addEventListener("submit", this.submit.bind(this));
    }

    submit(evt) {
      evt.preventDefault();
      this.post();
    }

    post() {
      const method = this.form.getAttribute('method'),
        path = this.form.getAttribute('action'),
        raw_url = this.form.querySelector('#original-url').value;

      var oReq = new XMLHttpRequest();
      oReq.addEventListener("load", this.onSuccess());
      oReq.addEventListener("error", this.onError.bind(this));

      oReq.open(method, path);
      oReq.setRequestHeader("Accept", "application/json");
      oReq.send(JSON.stringify({
        url: raw_url
      }));
    }

    onSuccess(a, b, c) {
      const _this = this;

      return function() {
        if (this.status > 400) {
          return _this.onError().bind(this)();
        }

        try {
          response = JSON.parse(this.responseText).short_code;
        } catch {
          response = this.responseText;
        }
        _this.error_text.innerHTML = '';
        _this.result_text.innerHTML = response;
      }
    }

    onError(resp) {
      const _this = this;
      return function() {
        resp = this.responseText || resp;
        _this.error_text.innerHTML = `${ERROR_MESSAGE} ${resp}`;
      }
    }

  }
  const body = document.querySelector('body');
  const page = new Page(body);
})()
