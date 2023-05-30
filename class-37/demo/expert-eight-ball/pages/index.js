import Head from 'next/head';
import { replies } from '../data';
import { useState } from 'react';

export default function Home() {

    const [question, setQuestion] = useState("Ask me anything...");
    const [reply, setReply] = useState("Thinking...");

    function questionAskedHandler(event) {
        event.preventDefault();
        setQuestion(event.target.question.value);
        event.target.reset();
        const randomReply = replies[Math.floor(Math.random() * replies.length)];
        setReply(randomReply);
    };

    return (
        <div className="">
            <Head>
                <title>Expert Eight Ball</title>
                <link rel="icon" href="/favicon.ico" />
            </Head>
            <Header />
            <main className="flex flex-col items-center py-4 space-y-8">
                <QuestionForm onSubmit={ questionAskedHandler } />
                <EightBall question={question} />
                <Response reply={reply} />
            </main>
            <Footer />
        </div>
    );
}

function Header() {
    return (
        <header className='p-4 text-4xl bg-gray-500 text-gray-50'>
            <h1>Expert 8 Ball</h1>
        </header>
    );
}

function Footer() {
    return (
        <footer className="p-4 mt-8 bg-gray-500 text-gray-50 ">
            <p>Expert Eight Ball &copy;{ new Date().getFullYear() }</p>
        </footer>
    );
}

function QuestionForm( props ) {
    return (
        <form onSubmit={ props.onSubmit } className="flex w-1/2 p-2 mx-auto my-4 bg-gray-200">
            <input name="question" className="flex-auto pl-1" />
            <button className="px-2 py-1 bg-gray-500 text-gray-50">Ask</button>
        </form>
    );
}

function EightBall(props) {
    return (
        <div className="mx-auto my-4 bg-gray-900 rounded-full w-96 h-96">
            <div className="relative flex items-center justify-center w-48 h-48 rounded-full bg-gray-50 top-16 left-16">
                <p className="text-xl text-center">{props.question}</p>
            </div>
        </div>
    );
}

function Response(props) {
    return (<p className="text-4xl text-center">{props.reply}</p>);
}
