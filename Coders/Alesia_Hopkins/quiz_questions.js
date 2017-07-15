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
		question: "Who was the co-inventor of the postet note?",
		answers: {
		  a: "Alexander Parkes",
		  b: "George Dixon",
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
	  },
	  {
		question: "What materials are stony meteors mainly composed of?",
		answers: {
		  a: " Silicate Minerals ",
		  b: " Zirconium ",
		  c: " Travertine",
		  d: " Cadmium "
		},
		correctAnswer: "a"
	},

	  {
		question: "When was Gold discovered?",
		answers: {
		  a: " 5000 BC ",
		  b: " 1000 AD ",
		  c: " 6000 BC ",
		  d: " 50 AD  "
		},
		correctAnswer: "c"
	  },
	  {
		question: "What do you call materials you can see through, such as glass?",
		answers: {
		  a: "Absorbent",
		  b: "Transparent",
		  c: "Opaque"
		},
		correctAnswer: "b"
	  },
	  {
		question: "What do you call the phase transition when solids change to gas?",
		answers: {
		  a: "Sublimination",
		  b: "Boiling",
		  c: "Melting"
		},
		correctAnswer: "a"
	  },
	  {
		question: "What is the change of state from gas to liquid called?",
		answers: {
		  a: "Ventilaton",
		  b: "Evaporation",
		  c: "Condensation",
		  d: "Sublimination"
		},
		correctAnswer: "c"
	  },
	  {
		question: "What is the symbol for the oxygen that we breath",
		answers: {
		  a: " Ox ",
		  b: " O1 ",
		  c: " OY",
		  d: " O2 "
		},
		correctAnswer: "d"
	},

	  {
		question: "How long has concrete been around",
		answers: {
		  a: " 1000 years",
		  b: " I Dunno ",
		  c: " 500 years ",
		  d: " 12,000,000 years  "
		},
		correctAnswer: "d"
	  },
	  {
		question: "Approximately, what percentage of an adult human is water?",
		answers: {
		  a: " 10%",
		  b: " 30% ",
		  c: " 90% ",
		  d: " 60%  "
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
