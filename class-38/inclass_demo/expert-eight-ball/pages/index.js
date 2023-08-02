import Head from 'next/head';
import { replies } from '@/data';
import { useState } from "react";

// New
import Header from '@/components/Header';
import Footer from '@/components/Footer';
import EightBall from '@/components/EightBall';
import QuestionForm from '@/components/QuestionForm';

export default function Home() {
    const [question, setQuestion] = useState('Ask me anything...');
    const [magicReplies, setMagicReplies] = useState([]);

    function questionAskedHandler(event) {
        event.preventDefault();
        setQuestion(event.target.question.value);
        const randomReply = replies[Math.floor(Math.random() * replies.length)];

        setMagicReplies([...magicReplies, randomReply]);
    }

    return(
        <div>

            <Head>
                <title>Expert 8 Ball</title>
                <link rel="icon" href="/favicon.ico" />
            </Head>

            {/* Header */}
            <Header />

            <main className="flex flex-col items-center py-4 space-y-8">

                {/* QuestionForm */}
                <QuestionForm questionAskedHandler={questionAskedHandler} />

                {/* Eight Ball */}
                <EightBall question={question} />

                {/* Replies(Table) */}
                <table>
                    <thead>
                        <tr>
                            <th>Replies:</th>
                        </tr>
                    </thead>
                    <tbody>
                        {/* conditional rendering */}
                        {
                            magicReplies.length > 0
                                ? magicReplies.map((magicReply, idx) => {
                                    return (
                                        <tr>
                                            <td>{magicReply}</td>
                                        </tr>
                                    )
                                })
                                : <tr>
                                    <td>Thinking...</td>
                                </tr>
                        }
                    </tbody>
                </table>

            </main>

            {/* Footer */}
            <Footer />
        </div>
    );
}
