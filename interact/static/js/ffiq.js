var $questionSolution = $('.questionSolution').attr('value')
var $description = $('#description')
var $questionTitle = $('#questionTitle')
var $answersChosen = $('.clicked')
var $descriptionButton = $('#descriptionButton')
var $titleButton = $('#titleButton')
var $selectButton = $('#selectButton')
var $nextPage = $('#nextPage')
var $answers = $('#selectionGroup')
var $isCorrect = false

$titleButton.hide()
$selectButton.hide()
$nextPage.hide()

$answers.click(function() {
  $selectButton.text('| The correct answer is ' + $questionSolution + ' shaded in.');
  $nextPage.show()
})

// check this function for is question correct
$nextPage.click(function() {
  checkAnswers()
  if ($isCorrect) {
    console.log('yay!')
    window.location.href = "/"}
  //   $curr = parseFloat(window.location.href.split('/')[4])
  //   $next = $curr + 1
  //   console.log($curr, typeof($curr))
  //   window.location.href = "/question/" + $next + "/"
  // }
})

$(window).on('load', function () {
  console.log('loaded');
  highlight($description, $descriptionButton);
  unhighlight($description, $descriptionButton, $questionTitle, $titleButton);
  unhighlight($questionTitle, $titleButton, $answers, $selectButton);
});

function highlight(focusPoint, focusButton) {
  focusPoint.css('border-style','solid')
  focusButton.show()
}

function unhighlight(focusPoint, focusButton, next, nextButton) {
  focusButton.on('click', function (){
    focusButton.hide()
    nextButton.show()
    focusPoint.css('border-style','none')
    highlight(next, nextButton)
  })
}

$("td").click(function(){
  $(this).toggleClass("clicked")
})


function checkAnswers() {
  var chosenAnswers = $('.clicked').each(function(index) {$(this).attr('value')})
  if (chosenAnswers.length == $questionSolution) {
        $isCorrect = true}}