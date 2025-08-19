import Head from 'next/head';

/**
 * CRM page
 *
 * A placeholder for managing contacts, leads, and clients. In a
 * production dashboard, this would be connected to your Airtable or
 * database. Here we display a static table to illustrate the layout.
 */
import { fetchContacts, ContactRecord } from '../lib/airtable';
import { GetServerSideProps } from 'next';

interface CRMProps {
  contacts: ContactRecord[];
}

export default function CRM({ contacts }: CRMProps) {
  return (
    <>
      <Head>
        <title>CRM · RiskTravel Dashboard</title>
      </Head>
      <main className="container">
        <h1>Customer Relationship Manager</h1>
        <p>
          Keep track of your leads, prospects and clients. This table pulls
          data from your Airtable base when the necessary environment
          variables are configured. Until then, the table will be empty.
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
            {contacts.length === 0 && (
              <tr>
                <td colSpan={4} style={{ padding: '0.5rem', textAlign: 'center' }}>
                  No contacts found. Once your agents begin collecting data and
                  syncing to Airtable, you’ll see records here.
                </td>
              </tr>
            )}
            {contacts.map((contact, index) => (
              <tr
                key={contact.id}
                style={{ backgroundColor: index % 2 === 0 ? '#f5f5fa' : '#ffffff' }}
              >
                <td style={{ padding: '0.5rem' }}>{contact.Name || '—'}</td>
                <td style={{ padding: '0.5rem' }}>{contact.Email || '—'}</td>
                <td style={{ padding: '0.5rem' }}>{contact.Persona || '—'}</td>
                <td style={{ padding: '0.5rem' }}>{contact.Stage || '—'}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </main>
    </>
  );
}

export const getServerSideProps: GetServerSideProps<CRMProps> = async () => {
  const contacts = await fetchContacts();
  return { props: { contacts } };
};