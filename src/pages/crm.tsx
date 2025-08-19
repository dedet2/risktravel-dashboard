import Head from 'next/head';

/**
 * CRM page
 *
 * A placeholder for managing contacts, leads, and clients. In a
 * production dashboard, this would be connected to your Airtable or
 * database. Here we display a static table to illustrate the layout.
 */
export default function CRM() {
  return (
    <>
      <Head>
        <title>CRM · RiskTravel Dashboard</title>
      </Head>
      <main className="container">
        <h1>Customer Relationship Manager</h1>
        <p>
          Keep track of your leads, prospects and clients. This table is a
          placeholder; connect it to Airtable or another CRM to populate it
          with real data.
        </p>
        <table style={{ width: '100%', borderCollapse: 'collapse', marginTop: '1rem' }}>
          <thead>
            <tr style={{ backgroundColor: 'var(--colour-grey-blue)', color: 'white' }}>
              <th style={{ padding: '0.5rem', textAlign: 'left' }}>Name</th>
              <th style={{ padding: '0.5rem', textAlign: 'left' }}>Email</th>
              <th style={{ padding: '0.5rem', textAlign: 'left' }}>Persona</th>
              <th style={{ padding: '0.5rem', textAlign: 'left' }}>Stage</th>
            </tr>
          </thead>
          <tbody>
            <tr style={{ backgroundColor: '#f5f5fa' }}>
              <td style={{ padding: '0.5rem' }}>Jane Merrick</td>
              <td style={{ padding: '0.5rem' }}>jane@example.com</td>
              <td style={{ padding: '0.5rem' }}>Merrick</td>
              <td style={{ padding: '0.5rem' }}>Initial Contact</td>
            </tr>
            <tr>
              <td style={{ padding: '0.5rem' }}>Kelly Lee</td>
              <td style={{ padding: '0.5rem' }}>kelly@example.com</td>
              <td style={{ padding: '0.5rem' }}>Kelly</td>
              <td style={{ padding: '0.5rem' }}>Engaged</td>
            </tr>
            <tr style={{ backgroundColor: '#f5f5fa' }}>
              <td style={{ padding: '0.5rem' }}>Javi Gomez</td>
              <td style={{ padding: '0.5rem' }}>javi@example.com</td>
              <td style={{ padding: '0.5rem' }}>Javi</td>
              <td style={{ padding: '0.5rem' }}>Booked Call</td>
            </tr>
            <tr>
              <td style={{ padding: '0.5rem' }}>Alex Johnson</td>
              <td style={{ padding: '0.5rem' }}>alex@example.com</td>
              <td style={{ padding: '0.5rem' }}>Whispering Pines Lead</td>
              <td style={{ padding: '0.5rem' }}>Deposit Paid</td>
            </tr>
          </tbody>
        </table>
      </main>
    </>
  );
}