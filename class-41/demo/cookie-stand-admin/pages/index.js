import Head from 'next/head';
import { useAuth } from '../contexts/auth';
import useResource from '../hooks/useResource';

export default function Home() {


    const { user, login, logout } = useAuth();
    const { resources, loading, createResource, deleteResource } = useResource();

    return (
        <div>
            <Head>
                <title>Cookie Stand Admin</title>
                <link rel="icon" href="/favicon.ico" />
            </Head>

            <main className="p-4 space-y-8 text-center">
                <h1 className="text-4xl">Fetching Data from Authenticated API</h1>
                {user ? (
                    <>
                        <h2>Welcome {user.username}</h2>
                        <button onClick={logout} className="p-2 text-white bg-gray-500 rounded">Logout</button>
                        <StandCreateForm onCreate={createResource} />
                        <StandList stands={resources} loading={loading} onDelete={deleteResource} />
                    </>
                ) : (
                    <>
                        <h2>Need to log in</h2>
                        <LoginForm onLogin={login} />
                    </>
                )}
            </main>

        </div>
    );
}

function LoginForm({ onLogin }) {

    async function handleSubmit(event) {
        event.preventDefault();
        onLogin(event.target.username.value, event.target.password.value);
    }

    return (
        <form onSubmit={handleSubmit}>
            <fieldset autoComplete='off'>
                <label htmlFor="username">Username</label>
                <input name="username" />
                <label htmlFor="password">Password</label>
                <input type="password" name="password" />
                <button>Log In</button>
            </fieldset>
        </form>
    );
}

function StandList({ stands, loading, onDelete }) {

    if (loading) { return <p>Loading...</p>; }

    return <ul>
        {stands.map(stand => (
            <>
                <li key={stand.id}>{stand.location}</li>
                <span onClick={() => onDelete(stand.id)}>[X]</span>
            </>
        ))}
    </ul>;
}


function StandCreateForm({ onCreate }) {

    function handleSubmit(event) {
        event.preventDefault();
        const standInfo = {
            location: event.target.location.value,
            minimum_customers_per_hour: parseInt(event.target.min.value),
            maximum_customers_per_hour: parseInt(event.target.max.value),
            average_cookies_per_sale: parseFloat(event.target.avg.value),
        };
        onCreate(standInfo);
        event.target.reset();
    }
    return (
        <form className="space-x-4" onSubmit={handleSubmit}>
            <input className="border-2 border-black" name="location" placeholder="location" />
            <input className="border-2 border-black" name="min" placeholder="min" />
            <input className="border-2 border-black" name="max" placeholder="max" />
            <input className="border-2 border-black" name="avg" placeholder="average" />
            <button className="p-2 text-white bg-gray-500 rounded">CREATE</button>
        </form>
    );
}


