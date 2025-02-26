import { Link, useNavigate, useParams } from "react-router";
import {
  useDeletePasswordProfileMutation,
  useGetPasswordProfileQuery,
} from "./passwordProfilesApi";
import { skipToken } from "@reduxjs/toolkit/query";
import { LoadingPage } from "../LoadingPage";
import { ExclamationCircleIcon } from "@heroicons/react/24/outline";
import PasswordProfile from "../passwordGeneration/PasswordProfile";
import { Button } from "../components/button";
import { Title } from "../components/heading";
import ConfirmDeleteModal from "../components/ConfirmDeleteModal";
import { useTranslation } from "react-i18next";

export default function PasswordProfilePage() {
  const { t } = useTranslation();
  const { id } = useParams();
  const navigate = useNavigate();
  const [deletePasswordProfile] = useDeletePasswordProfileMutation();

  const { data, isLoading } = useGetPasswordProfileQuery(
    id === undefined ? skipToken : id,
  );

  if (isLoading) {
    return <LoadingPage />;
  }

  if (!data) {
    return (
      <div>
        <div className="relative block w-full rounded-lg border-2 border-dashed border-gray-300 p-12 text-center hover:border-gray-400 focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 focus:outline-hidden">
          <ExclamationCircleIcon className="mx-auto size-12 text-gray-400" />
          <span className="mt-2 block text-sm font-semibold">
            {t("PasswordProfilePage.NoPasswordWithId", { id })}
          </span>
          <Link to="/passwordProfiles" className="text-sm">
            {t("PasswordProfilePage.GoListPasswordProfiles")}
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div>
      <div className="mb-2 flex items-center justify-between">
        <Title>
          {data.site}:{data.login}
        </Title>
        <ConfirmDeleteModal
          title={t("PasswordProfilePage.DeletePassword")}
          message={t("PasswordProfilePage.AreYouSure", {
            site: data.site,
            login: data.login,
          })}
          confirmTextButton={t("PasswordProfilePage.YesIAmSure")}
          cancelTextButton={t("PasswordProfilePage.NoIAmNotSure")}
          confirmed={() => {
            deletePasswordProfile(data);
            navigate("/passwordProfiles");
          }}
          button={(openModal) => (
            <Button type="submit" outline danger onClick={openModal}>
              {t("PasswordProfilePage.Delete")}
            </Button>
          )}
        />
      </div>
      <PasswordProfile
        passwordProfile={data}
        focus="masterPassword"
      ></PasswordProfile>
    </div>
  );
}
