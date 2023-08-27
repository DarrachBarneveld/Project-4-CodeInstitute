setTimeout(() => {
  let messages = document.getElementById("msg");
  let alert = new bootstrap.Alert(messages);
  alert.close();
}, 2500);

$(".counter").each(function () {
  const $this = $(this),
    countTo = $this.attr("data-to");
  countDuration = parseInt($this.attr("data-duration"));
  $({ counter: $this.text() }).animate(
    {
      counter: countTo,
    },
    {
      duration: countDuration,
      easing: "linear",
      step: function () {
        $this.text(Math.floor(this.counter));
      },
      complete: function () {
        $this.text(this.counter);
      },
    }
  );
});
