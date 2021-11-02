//login password validation
const strengthMeter             = document.getElementById('strength-meter')
const passwordInput             = document.getElementById('id_password1')
const confirmPasswordInput      = document.getElementById('id_password2')
const reasonsContainer          = document.getElementById('reasons')
const confirmReasonsContainer   = document.getElementById('confirm-reasons')


// An event listener that listens to the input from the password field and iterate through the functions
passwordInput.addEventListener('input',updateStrengthMeter)
confirmPasswordInput.addEventListener('blur',()=>{

    if (passwordInput.value != confirmPasswordInput.value){
        const message = "Passwords are not the same"
    }else{
        const message = ""
    }
    const messageConfirm = document.createElement('div')
    messageConfirm.innerText = message
    confirmReasonsContainer.appendChild(messageConfirm)
})
//Update the reasons of the password strength

function updateStrengthMeter(){
    const weaknesses = calculatePasswordStrength(passwordInput.value)
    let strength = 100
    reasonsContainer.innerHTML = ''
    weaknesses.forEach(weakness =>{
        if(weakness == null) return
        strength -= weakness.deduction
        const messageElement = document.createElement('div')
        messageElement.innerText = weakness.message
        reasonsContainer.appendChild(messageElement)
    })

    strengthMeter.style.setProperty('--strength',strength)
}

function calculatePasswordStrength(password){
    const weaknesses = []

    weaknesses.push(lengthWeakness(password))
    weaknesses.push(lowercaseWeakness(password))
    weaknesses.push(uppercaseWeakness(password))
    weaknesses.push(numberWeakness(password))
    weaknesses.push(specialCharactersWeakness(password))
    weaknesses.push(repeatCharacterWeakness(password))

    return weaknesses
}

function lengthWeakness(password){
    const length = password.length

    if(length <= 5){
        return {
            message : 'Your password is too short',
            deduction : 40
        }
    }
    if(length <=10){
        return{
            message:"Your password could be longer",
            deduction:15
        }
    }
}

function lowercaseWeakness(password){
    // /[a-z]/g this is a regular expression that has letters from a to z and is set to global
    return characterTypeWeakness(password , /[a-z]/g,"lowercase characters")
}

function uppercaseWeakness(password){
    return characterTypeWeakness(password , /[A-Z]/g,"uppercase characters")
}

function numberWeakness(password){
    return characterTypeWeakness(password , /[0-9]/g,"a numbers")
}

function specialCharactersWeakness(password){
    return characterTypeWeakness(password, /[^0-9a-zA-Z\s]/g,'special characters')
}




//this is used to avoid writing the same code in function:-
/*
        uppercaseWeakness
        lowercaseWeakness

*/
function characterTypeWeakness(password , regex , type){
    const matches = password.match(regex) || []


    if(matches.length <= 0 ){
        return {
            message:`Your password need to have ${type}`,
            deduction: 20

        }
    }
}

function repeatCharacterWeakness(password){

    const matches = password.match(/(.)\1/g) || []

    if(matches.length>0){
        return{
            message:"Your password has repeat characters more than twice",
            deduction:matches.length*10
        }
    }

}
//  show menu list

const navMenu   = document.getElementById('nav-menu'),
      navToggle = document.getElementById('nav-toggle'),
      navClose  = document.getElementById('nav-close')

     

if(navToggle){
    navToggle.addEventListener('click',()=>{
        navMenu.classList.add('show-menu')
    })
}

// HIDE MENU
// validate if constant exists
if(navClose){
    navClose.addEventListener('click' ,()=>{
        navMenu.classList.remove('show-menu')
    })
}    

/*==================== REMOVE MENU MOBILE ====================*/
const navLink = document.querySelectorAll('.nav__link')

function linkAction(){
    const navMenu = document.getElementById('nav-menu')
    // When we click on each nav__link, we remove the show-menu class
    navMenu.classList.remove('show-menu')
}
navLink.forEach(n => n.addEventListener('click', linkAction))


/*==================== CHANGE BACKGROUND HEADER ====================*/
function scrollHeader(){
    const header = document.getElementById('header')
    // When the scroll is greater than 100 viewport height, add the scroll-header class to the header tag
    if(this.scrollY >= 100) header.classList.add('scroll-header'); else header.classList.remove('scroll-header')
}
window.addEventListener('scroll', scrollHeader)
