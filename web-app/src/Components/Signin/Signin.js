
import React from 'react';

export default function Signin({onRouteChange}){
    const [signIn,setSignIn] = React.useState({
        signInEmail: '',
        signInPassword: ''
    })
    function handleChange(e){
        const {name,value} = e.target;
        setSignIn(prev => ({...prev,[name]:value}))
        console.log(signIn.signInEmail);
        console.log(signIn.signInPassword);
    }
    return(
        <article className="br3 ba dark-gray b--black-10 mv4 w-100 w-50-m w-25-l mw6 shadow-5">
                <main className="pa4 black-80 center">
                    <div className="measure tc">
                        <fieldset id="sign_up" className="ba b--transparent ph0 mh0">
                            <legend className="f1 fw6 ph0 mh0">Sign In</legend>
                            <div className="mt3">
                                <label className="db fw6 lh-copy f6" htmlFor="email-address">Email</label>
                                <input 
                                    className="pa2 input-reset ba bg-transparent hover-bg-black hover-white w-100"
                                    type="email" 
                                    name="signInEmail"  
                                    id="email-address"
                                    onChange={handleChange}
                                />
                            </div>
                            <div className="mv3">
                                <label className="db fw6 lh-copy f6" htmlFor="password">Password</label>
                                <input 
                                    className="b pa2 input-reset ba bg-transparent hover-bg-black hover-white w-100" 
                                    type="password" 
                                    name="signInPassword"  
                                    id="password" 
                                    onChange={handleChange}
                                />
                            </div>
                        </fieldset>
                        <div className="">
                            <input  
                                className="b ph3 pv2 input-reset ba b--black bg-transparent grow pointer f6 dib" 
                                type="submit"
                                value="Sign in"
                                // onSubmit={this.onSubmitSignIn}
                                // onClick={this.onSubmitSignIn} 
                            />
                        </div>
                        <div className="lh-copy mt3">
                            <p 
                                onClick={() => onRouteChange('register')}
                                className="f6 link dim black db pointer"
                            >
                                {'Register'}
                            </p>
                        </div>
                    </div>
                </main>
            </article>
    )
}