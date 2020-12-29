$.fn.jQuerySimpleCounter = function (options) {
  var settings = $.extend(
    {
      start: 0,
      end: 100,
      easing: "swing",
      duration: 400,
      complete: "",
    },
    options
  );

  var thisElement = $(this);

  $({ count: settings.start }).animate(
    { count: settings.end },
    {
      duration: settings.duration,
      easing: settings.easing,
      step: function () {
        var mathCount = Math.ceil(this.count);
        thisElement.text(mathCount);
      },
      complete: settings.complete,
    }
  );
};

$("#number1").jQuerySimpleCounter({ end: 30, duration: 1000 });
$("#number2").jQuerySimpleCounter({ end: 5655, duration: 1500 });
$("#number3").jQuerySimpleCounter({ end: 2944, duration: 2000 });
$("#number4").jQuerySimpleCounter({ end: 86, duration: 2500 });
