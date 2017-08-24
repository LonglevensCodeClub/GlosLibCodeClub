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
		console.log("answerContainers", answerContainers);
		console.log("questionNumber", questionNumber);
		if(userAnswer===currentQuestion.correctAnswer){
		  // add to the number of correct answers
		  numCorrect++;

		  // color the answers green
		  console.log("container", answerContainers[questionNumber]);

		  answerContainers[questionNumber].style.color = 'lightgreen';
		}
		else{
		  // if answer is wrong or blank - color the answers red
		  answerContainers[questionNumber].style.color = 'red';
		}
	  });

	  // show number of correct answers out of total
	  resultsContainer = document.getElementById('results');
	  resultsContainer.innerHTML = numCorrect + ' out of ' + myQuestions.length;
	  
	  submitButton=document.getElementById("Submit");
	  if (numCorrect < myQuestions.length) {
		  submitButton.innerHTML = "Try Again";
	  } else {
		  submitButton.innerHTML = "Well Done";
	      submitButton.onclick = function(){}
	  }
	}

	const myQuestions = [
	  {
		question: "When was Code Club founded?",
		answers: {
		  a: "2010",
		  b: "2011",
		  c: "2012"
		},
		correctAnswer: "c"
	  },
	  {
		question: "When did Code Club join forces with the Rasberry Pi Foundation?",
		answers: {
		  a: "2015",
		  b: "2013",
		  c: "2014"
		},
		correctAnswer: "a"
	  },
	  {
		question: "What age is Code Club aimed for?",
		answers: {
		  a: "9-10",
		  b: "5-8",
		  c: "6-10",
		  d: "9-11"
		},
		correctAnswer: "d"
	  },
	  {
		question: "Where is the most common place to book Code Club tickets?",
		answers: {
		  a: " Eventbrite ",
		  b: " Ticket Master ",
		  c: " CodeClub.org",
		},
		correctAnswer: "a"
	},

	  {
		question: "How many languages have Code Club projects been translated in?",
		answers: {
		  a: " 25 languages ",
		  b: " 20 languages ",
		  c: " 28 languages ",
		  d: " 32 languages "
		},
		correctAnswer: "c"
	  },
	  {
		question: "How much does Code Club cost?",
		answers: {
		  a: "Depends on age",
		  b: "It's Free",
		  c: "&pound;5 per session"
		},
		correctAnswer: "b"
	  },
	  {
		question: "Who has been teaching at code club the longest?",
		answers: {
		  a: "Steve ",
		  b: "Ben",
		  c: "Scott"
		},
		correctAnswer: "a"
	  },
	  {
		question: "Where  can you sign up to be a volounteer at Code Club now?",
		answers: {
		  a: "codeclub.net",
		  b: "codeclub.com",
		  c: "codeclub.org.uk",
		  d: "codeclub.to"
		},
		correctAnswer: "c"
	  },
	  {
		question: "Inside which HTML element do we put the javascript?",
		answers: {
		  a: " &lt;script+&gt; ",
		  b: " &lt;submit&gt;",
		  c: " &lt;scriptjs&gt;",
		  d: " &lt;script&gt; "
		},
		correctAnswer: "d"
	 },
	  {
		question: "What year did Longlevens Library Code Club begin?",
		answers: {
		  a: " 2015 October",
		  b: " 2014 October ",
		  c: " 2015 Janurary ",
		  d: " 2015 Janurary  "
		},
		correctAnswer: "a"
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
