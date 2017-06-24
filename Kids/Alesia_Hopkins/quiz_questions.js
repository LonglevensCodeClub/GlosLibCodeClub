//function generateQuiz(quizContainer, resultsContainer, submitButton){

	function showQuestions(questions, quizContainer){
	// we'll need a place to store the output and the answer choices
	var output = [];
	var answers;

	// for each question...
	for(var i=0; i<questions.length; i++){
		
		// first reset the list of answers
		answers = [];

		// for each available answer to this question...
		for(letter in questions[i].answers){

			// ...add an html radio button
			answers.push(
				'<label>'
					+ '<input type="radio" name="question'+i+'" value="'+letter+'">'
					+ letter + ': '
					+ questions[i].answers[letter]
				+ '</label>'
			);
		}

		// add this question and its answers to the output
		output.push(
			'<div class="question">' + questions[i].question + '</div>'
			+ '<div class="answers">' + answers.join('') + '</div>'
		);
	}

	// finally combine our output list into one string of html and put it on the page
	quizContainer = document.getElementById('quiz');
	quizContainer.innerHTML = output.join('');
	
	submitButton=document.getElementById("Submit");
		// when user clicks submit, show results
		submitButton.onclick = function(){
			showResults(myQuestions, quizContainer, resultsContainer);
		}
    }

	function showResults(){

	  // gather answer containers from our quiz
	  quizContainer = document.getElementById('quiz');
	  const answerContainers = quizContainer.querySelectorAll('.answers');

	  // keep track of user's answers
	  let numCorrect = 0;

	  // for each question...
	  myQuestions.forEach( (currentQuestion, questionNumber) => {

		// find selected answer
		const answerContainer = answerContainers[questionNumber];
		const selector = 'input[name=question'+questionNumber+']:checked';
		const userAnswer = (answerContainer.querySelector(selector) || {}).value;

		// if answer is correct
		if(userAnswer===currentQuestion.correctAnswer){
		  // add to the number of correct answers
		  numCorrect++;

		  // color the answers green
		  answerContainers[questionNumber].style.color = 'lightgreen';
		}
		// if answer is wrong or blank
		else{
		  // color the answers red
		  answerContainers[questionNumber].style.color = 'red';
		}
	  });

	  // show number of correct answers out of total
	  resultsContainer = document.getElementById('quiz');
	  resultsContainer.innerHTML = numCorrect + ' out of ' + myQuestions.length;
	  
	  submitButton=document.getElementById("Submit");
	  if (numCorrect < myQuestions.length) {
		  submitButton.text = "Try Again";
		  submitButton.onclick = function(){
			showQuestions(myQuestions, quizContainer, resultsContainer);
		 }
	  } else
		  submitButton.text = "Well Done";

		// show the questions
	//	showQuestions(myQuestions, quizContainer);

		// when user clicks submit, show results
		submitButton.onclick = function(){
			showResults(myQuestions, quizContainer, resultsContainer);
		}
	}

	const myQuestions = [
	  {
		question: "Who was the co-inventor of the postet note?",
		answers: {
		  a: "Alexander Parkes",
		  b: "Harry Brearley",
		  c: "Spencer Silver"
		},
		correctAnswer: "c"
	  },
	  {
		question: "Who was considered the creator of stainless steel?",
		answers: {
		  a: "Harry Brearley",
		  b: "Leo Beakeland",
		  c: "Georges de Mestral"
		},
		correctAnswer: "a"
	  },
	  {
		question: "The creator of lycra, Joseph C. Shivers, is ...?",
		answers: {
		  a: "Chinese",
		  b: "British",
		  c: "Japinese",
		  d: "American"
		},
		correctAnswer: "d"
	  }
	];


function buildQuiz(){
  // we'll need a place to store the HTML output
  const output = [];

  // for each question...
  myQuestions.forEach(
    (currentQuestion, questionNumber) => {

      // we'll want to store the list of answer choices
      const answers = [];

      // and for each available answer...
      for(letter in currentQuestion.answers){

        // ...add an HTML radio button
        answers.push(
          `<label>
            <input type="radio" name="question${questionNumber}" value="${letter}">
            ${letter} :
            ${currentQuestion.answers[letter]}
          </label>`
        );
      }

      // add this question and its answers to the output
		output.push(
			'<div class="question">' + currentQuestion.question + '</div>'
			+ '<div class="answers">' + answers.join('') + '</div>'
		);
    }
  );

  // finally combine our output list into one string of HTML and put it on the page
  quizContainer = document.getElementById('quiz');
  quizContainer.innerHTML = output.join('');
  
  resultsContainer = document.getElementById('results');
  	submitButton=document.getElementById("Submit");
	// when user clicks submit, show results
	submitButton.onclick = function(){
		showResults(myQuestions, quizContainer, resultsContainer);
	}
}


function showNextSlide() {
  showSlide(currentSlide + 1);
}

function showPreviousSlide() {
  showSlide(currentSlide - 1);
}

//previousButton = document.getElementById("previousButton")
//previousButton.addEventListener("click", showPreviousSlide);
//nextButton.addEventListener("click", showNextSlide);
//}
