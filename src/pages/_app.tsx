import '../styles/globals.css';
import type { AppProps } from 'next/app';
import Head from 'next/head';

/**
 * Custom App component to provide common layout elements and global styles.
 *
 * We define a simple header with navigation links using your brand
 * colours. All pages will be rendered inside this layout. You can
 * customise the header or add additional context providers here.
 */
export default function MyApp({ Component, pageProps }: AppProps) {
  return (
    <>
      <Head>
        {/* Import Google fonts for headings and body text */}
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link
          rel="preconnect"
          href="https://fonts.gstatic.com"
          crossOrigin=""
        />
        <link
          href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Roboto:wght@300;400;500;700&display=swap"
          rel="stylesheet"
        />
      </Head>
      <header className="app-header">
        <h1>RiskTravel</h1>
        <nav className="app-nav">
          {/* These links are placeholders. As you build out more pages
              (e.g. /agents, /metrics, /crm), update the hrefs accordingly. */}
          <a href="/">Home</a>
          <a href="#agents">Agents</a>
          <a href="#metrics">Metrics</a>
        </nav>
      </header>
      <Component {...pageProps} />
    </>
  );
}